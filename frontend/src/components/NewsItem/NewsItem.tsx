import React, { FC } from "react";
import { INews } from "../../models/INews";
import { Link } from "react-router-dom";
import s from "./NewsItem.module.scss";
import placeholder from "../../assets/img/placeholder.png";
import { Variants, motion } from "framer-motion";

interface NewsItemProps {
    news: INews;
    animationVariants?: Variants;
}

const NewsItem: FC<NewsItemProps> = ({ news, animationVariants }) => {
    const splitedMessage = news.msg.split(" ");
    const slicedMessage = splitedMessage.slice(0, 25);
    const cutMessage = slicedMessage.concat("...");
    const finalMessage = cutMessage.join(" ");

    return (
        <motion.li variants={animationVariants} className={s.item}>
            <div className={s.top}>
                <img
                    className={s.img}
                    src={news.photo ? news.photo : placeholder}
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
            </div>
        </motion.li>
    );
};

export default NewsItem;
