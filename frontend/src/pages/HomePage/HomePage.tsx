import s from "./HomePage.module.scss";
import { TypeAnimation } from "react-type-animation";

const HomePage = () => {
    return (
        <section>
            <div className={s.textContainer}>
                <h1 className={s.header}>
                    <TypeAnimation
                        sequence={[
                            "Подстройте",
                            2000,
                            "Разрежьте",
                            2000,
                            "Переделайте",
                            2000,
                            "Создайте",
                            2000,
                        ]}
                        wrapper="span"
                        speed={25}
                        style={{ display: "inline-block" }}
                        repeat={Infinity}
                    />
                    <span>новостную ленту под себя</span>
                </h1>
                <p className={s.text}>
                    Мы предоставляем сервис, который поможет вам настроить
                    новостную ленту таким образом, чтобы она показывала
                    исключительно то, что вас интересует. Чтобы добиться такого
                    результата мы используем ряд передовых технологий, которые
                    обеспечивают идеальный результат, удовлетворяющий
                    потребности любого пользователя вне зависимости от его
                    предпочтений!
                </p>
            </div>
            <button className={s.btn}>Начать пользоваться сейчас</button>
        </section>
    );
};

export default HomePage;
