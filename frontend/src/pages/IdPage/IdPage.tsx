import React from 'react';
import { useParams } from 'react-router-dom';
import s from "./IdPage.module.scss";

const IdPage = () => {
  const { news } = useParams();
  console.log(news)

  return (
    <div></div>
  );
};

export default IdPage;