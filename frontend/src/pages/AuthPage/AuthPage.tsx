import { useEffect, useState } from "react";
import { useLoginUserMutation } from "../../services/authApi";
import { useNavigate, Link } from "react-router-dom";
import { motion } from "framer-motion";
import { useAppDispatch } from "../../app/hooks";
import { setUser } from "../../features/authSlice";
import { toast } from "react-toastify";
import s from "./AuthPage.module.scss";

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
            console.log("Заполните все поля ввода");
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
        <motion.section
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
            className={s.section}
        >
            <div className={s.container}>
                <h2 className={s.header}>Авторизация</h2>
                <div className={s.credentials}>
                    <input
                        className={s.input}
                        type="email"
                        name="email"
                        value={formValue.email}
                        onChange={handleChange}
                        placeholder="Email"
                    />
                    <input
                        className={s.input}
                        type="password"
                        name="password"
                        value={formValue.password}
                        onChange={handleChange}
                        placeholder="Пароль"
                    />
                    <div className={s.btnContainer}>
                        <button
                            type="button"
                            className={s.btn}
                            onClick={handleLogin}
                        >
                            Войти
                        </button>
                    </div>
                    <div className={s.attention}>
                        <p>
                            Нет аккаунта? <Link to="/register">Зарегистрироваться</Link>
                        </p>
                    </div>
                </div>
            </div>
        </motion.section>
    );
};

export default AuthPage;
