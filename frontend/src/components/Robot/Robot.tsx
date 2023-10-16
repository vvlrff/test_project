import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment, ContactShadows } from "@react-three/drei";
import { Model } from "./Tg";
import s from "./Robot.module.scss";

const Robot = () => {
    return (
        <Canvas
            className={s.model}
            shadows
            camera={{ position: [0, 0, 6], fov: 20 }}
        >
            <ambientLight intensity={2.25} />
            <ambientLight intensity={0.1} />
            <directionalLight intensity={0.4} />
            <Model scale={0.8}></Model>
            {/* <ContactShadows position={[0, -0.8, 0]} color="#ffffff" /> */}
            <OrbitControls
                autoRotateSpeed={5}
                autoRotate
                minPolarAngle={Math.PI / 2}
                maxPolarAngle={Math.PI / 2}
                enableZoom={false}
            />
        </Canvas>
    );
};

export default Robot;
