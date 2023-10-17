import React, { FC } from "react";
import { INews } from "../../models/INews";
import { Link } from "react-router-dom";
import s from "./NewsItem.module.scss";
import { Variants, motion } from "framer-motion";

interface NewsItemProps {
    news: INews;
    animationVariants?: Variants;
}

const NewsItem: FC<NewsItemProps> = ({ news, animationVariants }) => {
    const splitedMessage = news.msg.split(" ");
    const slicedMessage = splitedMessage.slice(0, 35);
    const cutMessage = slicedMessage.concat("...");
    const finalMessage = cutMessage.join(" ");

    const dateTime = news.date.split("T");

    return (
        <motion.li variants={animationVariants} className={s.item}>
            <div className={s.top}>
                <img
                    className={s.img}
                    src={news.photo}
                    alt="photoImg"
                />
            </div>
            <div className={s.content}>
                <p className={s.text}>{finalMessage}</p>
                <div className={s.buttonContainer}>
                    <Link to={`/news/${news.id}`} className={s.button}>
                        Подробнее
                    </Link>
                </div>
                <div className={s.dateContainer}>
                    <p className={s.date}>{dateTime[0]}</p>
                    <p className={s.time}>{dateTime[1]}</p>
                </div>
            </div>
        </motion.li>
    );
};

export default NewsItem;
