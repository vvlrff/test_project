import s from "./MessageLoader.module.scss";

const MessageLoader = () => {
    return (
        <div className={s.ldsEllipsis}>
            <div className={s.container}>
                <div className={s.ellipsis}></div>
                <div className={s.ellipsis}></div>
                <div className={s.ellipsis}></div>
                <div className={s.ellipsis}></div>
            </div>
        </div>
    );
};

export default MessageLoader;
