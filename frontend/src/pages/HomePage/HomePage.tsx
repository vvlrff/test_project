import { useState } from 'react';
import Hero from "./Hero/Hero";
import Channels from "./Channels/Channels";
import HowTo from "./HowTo/HowTo";

const HomePage = () => {
    const [condition, setCondition] = useState<number>(4)

    const handleCondition = (): void => {
        setCondition(prev => prev - 1)
    }

    const handleScrollDown = (): void => {
        handleCondition()
    }

    return (
        <>
            <Hero></Hero>
            <Channels handleCondition={handleCondition} condition={condition} handleScrollDown={handleScrollDown}></Channels>
            {condition < 1 ? <HowTo /> : null}
        </>
    );
};

export default HomePage;
