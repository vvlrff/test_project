import React from 'react';
import { useParams } from 'react-router-dom';
import s from "./IdPage.module.scss";

const IdPage = () => {
  const { id } = useParams();
  console.log(id)

  return (
    <div>{id}</div>
  );
};

export default IdPage;