import { useState } from "react";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { newsApi } from "../../services/newsApi";
import NewsItem from "../../components/NewsItem/NewsItem";
import { motion } from "framer-motion";
import s from "./NewsPage.module.scss";
import Loader from "../../components/Loader/Loader";
import Error from "../../components/Error/Error";
// import { AiOutlineSearch } from "react-icons/ai";
// import data from "./fakeNews";

const NewsPage = () => {
    const [startDate, setStartDate] = useState<any>([]);
    const [endDate, setEndDate] = useState<any>([]);
    const [message, setMessage] = useState<string>("");
    const [isFilterOpen, setIsFilterOpen] = useState<boolean>(false);
    const [sortOption, setSortOption] = useState<string>("new");

    const {
        data: news,
        error,
        isLoading,
    } = newsApi.useGetAllNewsQuery(sortOption);


    const [
        requestMessage,
        {
            data: requestMessageData,
            isSuccess: isMessageSuccess,
            isLoading: isMessageRequestLoading,
            error: requestMessageError,
        },
    ] = newsApi.usePostAllNewsMessageMutation();

    const [
        request,
        {
            data: requestData,
            isSuccess,
            isLoading: isRequestLoading,
            error: requestError,
        },
    ] = newsApi.usePostAllNewsMutation();

    const resetFilters = () => {
        window.location.reload();
    };

    const handleOpen = (): void => {
        setIsFilterOpen(true);
    };

    const handleClose = (): void => {
        setIsFilterOpen(false);
    };

    const handleSortChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setSortOption(event.target.value);
    };

    const sendData = async () => {
        await request({
            message: message,
            start_date: startDate.toISOString(),
            end_date: endDate.toISOString(),
        });
    };

    const sendDataMessage = async () => {
        await requestMessage({
            message: message
        });
    };

    const listV = {
        hidden: { opacity: 0 },
        visible: {
            opacity: 1,
            transition: {
                duration: 0.5,
                delayChildren: 0.8,
                staggerChildren: 0.2,
            },
        },
    };

    const itemV = {
        hidden: { y: 20, opacity: 0 },
        visible: {
            y: 0,
            opacity: 1,
        },
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
                    {!isFilterOpen && <button className={s.btn} onClick={() => sendDataMessage()}>Искать</button>}
                    {/* <AiOutlineSearch /> */}
                </div>

                <div className={s.dates}>
                    <section>
                        <select onChange={handleSortChange}>
                            <option value="new">Сначала новые</option>
                            <option value="old">Сначала старые</option>
                        </select>
                    </section>
                    {isFilterOpen ? (
                        <>
                            <button className={s.btn} onClick={() => handleClose()}>
                                Скрыть фильтр
                            </button>
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
                                {isSuccess && (
                                    <button
                                        className={s.btn}
                                        onClick={() => resetFilters()}
                                    >
                                        Сбросить фильтры
                                    </button>
                                )}
                            </LocalizationProvider>
                        </>
                    ) : (
                        <button className={s.btn} onClick={() => handleOpen()}>
                            Временной фильтр
                        </button>
                    )}
                </div>
            </div>

            <div className={s.content}>
                {isMessageSuccess ? (
                    <motion.ul
                        initial="hidden"
                        animate="visible"
                        variants={listV}
                        className={s.list}
                    >
                        {isMessageRequestLoading && <Loader></Loader>}
                        {requestMessageError && <Error></Error>}
                        {requestMessageData?.map((requestDataItem) => (
                            <NewsItem
                                key={requestDataItem.id}
                                news={requestDataItem}
                                animationVariants={itemV}
                            />
                        ))}
                    </motion.ul>
                ) : isSuccess ? (
                    <motion.ul
                        initial="hidden"
                        animate="visible"
                        variants={listV}
                        className={s.list}
                    >
                        {isRequestLoading && <Loader></Loader>}
                        {requestError && <Error></Error>}
                        {requestData?.map((requestDataItem) => (
                            <NewsItem
                                key={requestDataItem.id}
                                news={requestDataItem}
                                animationVariants={itemV}
                            />
                        ))}
                    </motion.ul>
                ) : (
                    <>
                        {isLoading && <Loader></Loader>}
                        {error && <Error></Error>}
                        <motion.ul
                            initial="hidden"
                            animate="visible"
                            variants={listV}
                            className={s.list}
                        >
                            {news?.map((newsItem) => (
                                <NewsItem
                                    key={newsItem.id}
                                    news={newsItem}
                                    animationVariants={itemV}
                                />
                            ))}
                        </motion.ul>
                    </>
                )
                }
            </div>
        </section>
    );
};

export default NewsPage;