import { useState } from "react";
import s from "./PostPage.module.scss"
import { postApi } from "../../services/postApi";
import { useAppDispatch } from "../../app/hooks";
import PostItem from "../../components/PostItem";

const PostPage = () => {
    const [searchFetch, setSearchFetch] = useState('');
    const { data: posts, error, isLoading } = postApi.useGetAllPostsQuery(5);
    const dispatch = useAppDispatch();


    return (
        <div>
            <input
                placeholder="Поиск новостей"
                value={searchFetch}
                onChange={(e) => setSearchFetch(e.target.value)}
                type="text"
            />

            <div>
                {isLoading && <h1>Идет загрузка</h1>}
                {error && <h1>Произошла ошибка</h1>}
                {posts?.map(post => <PostItem key={post.id} post={post} />)}
            </div>
        </div>
    );
};

export default PostPage;