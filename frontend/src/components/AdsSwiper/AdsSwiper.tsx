import { Swiper, SwiperSlide } from 'swiper/react'
import 'swiper/css'
import { Autoplay } from 'swiper'
import ad from '../../assets/img/ads.svg'


const AdsSwiper = () => {
    return (
        <Swiper
            className="sample-slider"
            modules={[Autoplay]}
            loop={true}
            autoplay={{
                delay: 0,
            }}
            slidesPerView={7}
            spaceBetween={200}
            speed={2000}
        >
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>
            <SwiperSlide><img src={ad} alt='' /></SwiperSlide>

        </Swiper>
    );
}

export default AdsSwiper;