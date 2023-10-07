import { useState } from "react";
import { newsApi } from "../../services/newsApi";
import NewsItem from "../../components/NewsItem/NewsItem";
import s from "./NewsPage.module.scss"

const NewsPage = () => {
    const [searchRequest, setSearchRequest] = useState('');
    const { data: news, error, isLoading } = newsApi.useGetAllNewsQuery(searchRequest);

    return (
        <div>
            <input
                placeholder="Поиск новостей"
                value={searchRequest}
                onChange={(e) => setSearchRequest(e.target.value)}
                type="text"
            />

            <div className={s.container}>
                {isLoading && <h1>Идет загрузка</h1>}
                {error && <h1>Произошла ошибка</h1>}
                {news?.map(newsItem => <NewsItem key={newsItem.id} news={newsItem} />)}
            </div>
        </div>
    );
};

export default NewsPage;