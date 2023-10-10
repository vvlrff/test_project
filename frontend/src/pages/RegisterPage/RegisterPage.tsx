import { useState, useEffect } from "react";
import { useRegisterUserMutation } from "../../services/authApi";
import { useNavigate } from "react-router-dom";

const initialState = {
  email: "",
  name: "",
  password: "",
};

const RegisterPage = () => {
  const [formValue, setFormValue] = useState(initialState);
  const { email, name, password } = formValue;
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
    if (email && name && password) {
      await registerUser({
        email, name, password, role_id: 0
      });
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
          name="name"
          value={name}
          onChange={handleChange}
          placeholder="ФИО"
        />
        <input
          type="password"
          name="password"
          value={password}
          onChange={handleChange}
          placeholder="Пароль"
        />
        <button type="button" onClick={() => handleRegister()}>
          Зарегистрироваться
        </button>
      </section>
    </div>
  );
};

export default RegisterPage;