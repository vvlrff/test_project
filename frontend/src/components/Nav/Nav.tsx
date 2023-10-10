import { NavLink } from "react-router-dom";
import s from "./Nav.module.scss";

const Nav = () => {
    return (
        <nav className={s.nav}>
            <div className={s.left}>
                <img
                    src="https://thumb.tildacdn.com/tild3237-3232-4266-a362-333130353936/-/resize/104x/-/format/webp/_____2__1.png"
                    alt=""
                />
            </div>
            <div className={s.right}>
                <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/">
                    Главная{" "}
                </NavLink>
                <NavLink className={({ isActive }) => !isActive ? `${s.link}` : `${s.active} ${s.link}`} to="/news">
                    Новости{" "}
                </NavLink>
            </div>
        </nav>
    );
};

export default Nav;
