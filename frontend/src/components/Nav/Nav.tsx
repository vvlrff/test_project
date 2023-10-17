import { NavLink } from "react-router-dom";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { logout, selectAuth } from "../../features/authSlice";
import { BsTelegram } from "react-icons/bs";
import s from "./Nav.module.scss";

const Nav = () => {
    const { access_token } = useAppSelector(selectAuth);
    const dispatch = useAppDispatch();

    const handleLogout = () => {
        dispatch(logout());
    };

    return (
        <nav className={s.nav}>
            <div className={s.left}>
                <img
                    src="https://thumb.tildacdn.com/tild3237-3232-4266-a362-333130353936/-/resize/104x/-/format/webp/_____2__1.png"
                    alt="logo"
                />
                <a href="https://t.me/AI_News_GPT_Bot">
                    <BsTelegram style={{ width: 25, height: 25 }} />
                </a>
            </div>
            <div className={s.right}>
                {access_token ? (
                    <>
                        <NavLink
                            className={({ isActive }) =>
                                !isActive
                                    ? `${s.link}`
                                    : `${s.active} ${s.link}`
                            }
                            to="/"
                        >
                            Главная{" "}
                        </NavLink>
                        <NavLink
                            className={({ isActive }) =>
                                !isActive
                                    ? `${s.link}`
                                    : `${s.active} ${s.link}`
                            }
                            to="/news"
                        >
                            Новости{" "}
                        </NavLink>
                        <NavLink
                            className={s.link}
                            to="/"
                            onClick={() => handleLogout()}
                        >
                            Выйти{" "}
                        </NavLink>
                    </>
                ) : (
                    <>
                        <NavLink
                            className={({ isActive }) =>
                                !isActive
                                    ? `${s.link}`
                                    : `${s.active} ${s.link}`
                            }
                            to="/"
                        >
                            Главная{" "}
                        </NavLink>
                        {/* <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/register">
                            Зарегистрироваться{" "}
                        </NavLink> */}
                        <NavLink
                            className={({ isActive }) =>
                                !isActive
                                    ? `${s.link}`
                                    : `${s.active} ${s.link}`
                            }
                            to="/auth"
                        >
                            Войти{" "}
                        </NavLink>
                    </>
                )}
            </div>
        </nav>
    );
};

export default Nav;
