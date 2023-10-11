import { NavLink } from "react-router-dom";
import s from "./Nav.module.scss";
import { isUserAuthenticated } from "../../cookie/isUserAuthenticated ";
import { useLogoutUserMutation } from "../../services/authApi";

const Nav = () => {
    const [logoutUser,
        {
            isSuccess,
            isError,
            error
        }
    ] = useLogoutUserMutation();

    const handleLogout = () => {
        logoutUser("");
    }

    return (
        <nav className={s.nav}>
            <div className={s.left}>
                <img
                    src="https://thumb.tildacdn.com/tild3237-3232-4266-a362-333130353936/-/resize/104x/-/format/webp/_____2__1.png"
                    alt=""
                />
            </div>
            <div className={s.right}>
                {!isUserAuthenticated ? (
                    <>
                        <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/">
                            Главная{" "}
                        </NavLink>
                        <NavLink className={s.link} to="/chat">
                            Чат{" "}
                        </NavLink>
                        <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/news">
                            Новости{" "}
                        </NavLink>
                        <NavLink className={s.link} to="/" onClick={() => handleLogout()}>
                            Выйти{" "}
                        </NavLink>
                    </>
                ) : (
                    <>
                        <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/">
                            Главная{" "}
                        </NavLink>
                        {/* <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/register">
                            Зарегистрироваться{" "}
                        </NavLink> */}
                        <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/auth">
                            Войти{" "}
                        </NavLink>
                    </>

                )}
            </div>
        </nav>
    );
};

export default Nav;
