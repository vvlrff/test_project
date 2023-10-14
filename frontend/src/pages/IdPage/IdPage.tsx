import React from 'react';
import { useParams } from 'react-router-dom';
import { newsApi } from '../../services/newsApi';
import s from "./IdPage.module.scss";

const IdPage = () => {
  const { id } = useParams();
  const numberId = Number(id)
  
  const {
    data,
    error,
    isLoading,
} = newsApi.useGetNewsQuery(numberId);

  return (
    <div>
      <div>{data?.id}</div>  
      <div>{data?.date}</div> 
      <img src={data?.photo} alt="photo"/>
      <div>{data?.msg}</div> 
      <div>{data?.url}</div> 
    </div>
  );
};

export default IdPage;