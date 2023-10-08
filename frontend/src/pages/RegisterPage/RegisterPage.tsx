import { useState, useEffect } from "react";
import { useRegisterUserMutation } from "../../services/authApi";
import { useNavigate } from "react-router-dom";

const initialState = {
  email: "",
  fullname: "",
  username: "",
  password: "",
  confirmPassword: ""
};

const RegisterPage = () => {
  const [formValue, setFormValue] = useState(initialState);
  const { email, fullname, username, password, confirmPassword } = formValue;
  const navigate = useNavigate();

  const [registerUser,
    {
      isSuccess: isRegisterSuccess,
      isError: isRegisterError,
      error: registerError
    }
  ] = useRegisterUserMutation();

  const handleChange = (e: any) => {
    setFormValue({ ...formValue, [e.target.name]: e.target.value });
  };

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      console.log("Пароли не совпадают");
    }

    if (email && fullname && username && password) {
      await registerUser({ email, fullname, username, password, confirmPassword });
    }
  }

  useEffect(() => {
    if (isRegisterSuccess) {
      console.log("Пользователь успешно зарегистрирован");
      navigate("/auth");
    }
  }, [isRegisterSuccess]);

  useEffect(() => {
    if (isRegisterError) {
      console.log((registerError as any).data.message);
    }
  }, [isRegisterError]);

  return (
    <div>
      <h2>Регистрация</h2>
      <section>
        <input
          type="email"
          name="email"
          value={email}
          onChange={handleChange}
          placeholder="Email"
        />
        <input
          type="text"
          name="fullname"
          value={fullname}
          onChange={handleChange}
          placeholder="ФИО"
        />
        <input
          type="text"
          name="username"
          value={username}
          onChange={handleChange}
          placeholder="Имя пользователя"
        />
        <input
          type="password"
          name="password"
          value={password}
          onChange={handleChange}
          placeholder="Пароль"
        />
        <input
          type="password"
          name="confirmPassword"
          value={confirmPassword}
          onChange={handleChange}
          placeholder="Повторите пароль"
        />
        <button type="button" onClick={() => handleRegister()}>
          Зарегистрироваться
        </button>
      </section>
    </div>
  );
};

export default RegisterPage;