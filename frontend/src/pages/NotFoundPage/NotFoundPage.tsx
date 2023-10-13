import { Link } from "react-router-dom";
import s from "./NotFoundPage.module.scss";

const NotFoundPage = () => {
    return (
        <section className={s.section}>
            <div className={s.container}>
                <p className={s.bigText}>Упс...</p>
                <p className={s.text}>Такой страницы не существует</p>
                <Link to="/" className={s.link}>
                    Вернуться на главную
                </Link>
            </div>
        </section>
    );
};

export default NotFoundPage;
