import { useState } from "react";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { newsApi } from "../../services/newsApi";
import NewsItem from "../../components/NewsItem/NewsItem";
import s from "./NewsPage.module.scss";
import Loader from "../../components/Loader/Loader";
// import { AiOutlineSearch } from "react-icons/ai";

const NewsPage = () => {
    const [startDate, setStartDate] = useState<any>([]);
    const [endDate, setEndDate] = useState<any>([]);
    const [message, setMessage] = useState("");

    const {
        data: news,
        error,
        isLoading,
    } = newsApi.useGetAllNewsQuery(message);

    const [
        request,
        { data: requestData, isSuccess, isLoading: isRequestLoading, error: requestError },
    ] = newsApi.usePostAllNewsMutation();

    const resetFilters = () => {
        window.location.reload();
    };

    const sendData = async () => {
        await request({
            message: message,
            start_date: startDate.toISOString(),
            end_date: endDate.toISOString(),
        });
    };

    return (
        <section className={s.news}>
            <div className={s.search}>
                <div className={s.searchLineContainer}>
                    <input
                        className={s.searchInput}
                        placeholder="Поиск новостей"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        type="text"
                    />
                    {/* <AiOutlineSearch /> */}
                </div>

                <div className={s.dates}>
                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DatePicker
                            label="От"
                            value={startDate}
                            onChange={(newValue) => setStartDate(newValue)}
                        />
                        <DatePicker
                            label="До"
                            value={endDate}
                            onChange={(newValue) => setEndDate(newValue)}
                        />
                        <button className={s.btn} onClick={() => sendData()}>
                            Искать
                        </button>
                        {isSuccess && (<button className={s.btn} onClick={() => resetFilters()}>Сбросить фильтры</button>)}
                    </LocalizationProvider>
                </div>
            </div>


            <div className={s.content}>
                {isSuccess ? (
                    <div className={s.container}>
                        {isRequestLoading && <Loader></Loader>}
                        {requestError && <h1>Произошла ошибка requestError</h1>}
                        {requestData?.map((requestDataItem) => (
                            <NewsItem
                                key={requestDataItem.id}
                                news={requestDataItem}
                            />
                        ))}
                    </div>
                ) : (
                    <div className={s.container}>
                        {isLoading && <Loader></Loader>}
                        {error && <h1>Произошла ошибка</h1>}
                        {news?.map((newsItem) => (
                            <NewsItem key={newsItem.id} news={newsItem} />
                        ))}
                    </div>
                )}


            </div>
        </section>
    );
};

export default NewsPage;
