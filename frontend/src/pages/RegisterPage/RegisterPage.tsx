import { useState, useEffect } from "react";
import { useRegisterUserMutation } from "../../services/authApi";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import s from "./RegisterPage.module.scss";

const initialState = {
    email: "",
    name: "",
    password: "",
};

const RegisterPage = () => {
    const [formValue, setFormValue] = useState(initialState);
    const { email, name, password } = formValue;
    const navigate = useNavigate();

    const [
        registerUser,
        {
            isSuccess: isRegisterSuccess,
            isError: isRegisterError,
            error: registerError,
        },
    ] = useRegisterUserMutation();

    const handleChange = (e: any) => {
        setFormValue({ ...formValue, [e.target.name]: e.target.value });
    };

    const handleRegister = async () => {
        if (email && name && password) {
            await registerUser({
                email,
                name,
                password,
                role_id: 0,
            });
        }
    };

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
        <motion.section
            className={s.section}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
        >
            <div className={s.container}>
                <h2 className={s.header}>Регистрация</h2>
                <div className={s.credentials}>
                    <input
                        className={s.input}
                        type="email"
                        name="email"
                        value={email}
                        onChange={handleChange}
                        placeholder="Email"
                    />
                    <input
                        className={s.input}
                        type="text"
                        name="name"
                        value={name}
                        onChange={handleChange}
                        placeholder="ФИО"
                    />
                    <input
                        className={s.input}
                        type="password"
                        name="password"
                        value={password}
                        onChange={handleChange}
                        placeholder="Пароль"
                    />
                </div>
                <div className={s.btnContainer}>
                    <button
                        type="button"
                        className={s.btn}
                        onClick={() => handleRegister()}
                    >
                        Зарегистрироваться
                    </button>
                </div>
            </div>
        </motion.section>
    );
};

export default RegisterPage;
