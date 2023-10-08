import { useEffect, useState } from "react";
import { useLoginUserMutation } from "../../services/authApi";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import { useAppDispatch } from "../../app/hooks";
import { setUser } from "../../features/authSlice";

const initialState = {
  email: "",
  password: ""
};

const AuthPage = () => {
  const [formValue, setFormValue] = useState(initialState);

  const { email, password } = formValue;
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
    if (email && password) {
      await loginUser({ email, password });
    } else {
      toast.error("Заполните все поля ввода")
    }
  };

  const handleChange = (e: any) => {
    setFormValue({ ...formValue, [e.target.name]: e.target.value });
  };

  useEffect(() => {
    if (isLoginSuccess) {
      toast.success("Пользователь успешно авторизирован");
      dispatch(setUser({ email: loginData.email, accessToken: loginData.accessToken }));
      navigate("/posts");
    }
  }, [isLoginSuccess]);

  useEffect(() => {
    if (isLoginError) {
      toast.error((loginError as any).data.message);
    }
  }, [isLoginError]);

  return (
    <div>
      <h2>Авторизация</h2>
      <section>
        <input
          type="email"
          name="email"
          value={email}
          onChange={handleChange}
          placeholder="Email"
        />
        <input
          type="password"
          name="password"
          value={password}
          onChange={handleChange}
          placeholder="Пароль"
        />
        <button type="button" onClick={() => handleLogin()}>
          Войти
        </button>
      </section>
    </div>
  );
};

export default AuthPage;