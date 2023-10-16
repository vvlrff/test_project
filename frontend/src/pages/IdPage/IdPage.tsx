import React from "react";
import { useParams } from "react-router-dom";
import { newsApi } from "../../services/newsApi";
import s from "./IdPage.module.scss";

const IdPage = () => {
    const { id } = useParams();
    const numberId = Number(id);

    const { data, error, isLoading } = newsApi.useGetNewsQuery(numberId);

    return (
        <section className={s.section}>
            <img src={data?.photo} className={s.img} alt="articlePhoto" />
            <div className={s.content}>
                <p className={s.text}>{data?.msg}</p>
                <div className={s.miscContainer}>
                    <div className={s.date}>Дата публикации: {data?.date}</div>
                    <div className={s.source}>Источник: {data?.url}</div>
                </div>
            </div>
        </section>
    );
};

export default IdPage;
