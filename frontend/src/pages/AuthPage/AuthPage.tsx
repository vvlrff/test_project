import { useEffect, useState } from "react";
import { useLoginUserMutation } from "../../services/authApi";
import { useNavigate } from "react-router-dom";
import { useAppDispatch } from "../../app/hooks";
import { setUser } from "../../features/authSlice";
import { toast } from "react-toastify";

const AuthPage = () => {
  const [formValue, setFormValue] = useState({
    email: "",
    password: "",
  });

  const navigate = useNavigate();
  const dispatch = useAppDispatch();

  const [loginUser,
    {
      data: loginData,
      isSuccess: isLoginSuccess,
      isError: isLoginError,
      error: loginError
    }
  ] = useLoginUserMutation();

  const handleLogin = async () => {
    const formData = new FormData();
    formData.append("username", formValue.email);
    formData.append("password", formValue.password);

    if (formValue.email && formValue.password) {
      await loginUser(formData);
    } else {
      console.log("Заполните все поля ввода")
    }
  };

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setFormValue({ ...formValue, [name]: value });
  };

  useEffect(() => {
    if (isLoginSuccess) {
      console.log("Пользователь успешно авторизирован");
      dispatch(setUser({ access_token: loginData.access_token }));
      navigate("/news");
    }
  }, [isLoginSuccess]);

  useEffect(() => {
    if (isLoginError) {
      console.log((loginError as any).data.message);
    }
  }, [isLoginError]);

  return (
    <div>
      <h2>Авторизация</h2>
      <section>
        <input
          type="email"
          name="email"
          value={formValue.email}
          onChange={handleChange}
          placeholder="Email"
        />
        <input
          type="password"
          name="password"
          value={formValue.password}
          onChange={handleChange}
          placeholder="Пароль"
        />
        <button type="button" onClick={handleLogin}>
          Войти
        </button>
      </section>
    </div>
  );
};

export default AuthPage;
