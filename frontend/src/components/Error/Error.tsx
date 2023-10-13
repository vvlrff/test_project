import s from "./Error.module.scss";
import { FC } from "react";

interface IError {}

const Error: FC<IError> = () => {
    return (
        <div className={s.container}>
            <p className={s.bigText}>Ой всё</p>
            <p className={s.text}>Что-то пошло не так...</p>
            {/* {text ? <p className={s.smallText}>Произошла {text}</p> : null} */}
        </div>
    );
};

export default Error;
