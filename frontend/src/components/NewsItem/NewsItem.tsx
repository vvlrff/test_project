import React, { FC } from 'react'
import { INews } from '../../models/INews';
import s from "./NewsItem.module.scss"

interface NewsItemProps {
    news: INews;
};

const NewsItem: FC<NewsItemProps> = ({ news }) => {
    const handleDelete = () => {

    }
    
    return (
        <div className={s.container}>
            <img className={s.img} src={news.photo} alt='photo'/>
            <div>{news.msg}</div>
            <div>{news.date}</div>
            <button onClick={() => handleDelete()}>Удалить</button>
        </div>
    );
};

export default NewsItem;