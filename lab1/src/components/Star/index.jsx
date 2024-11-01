import React from 'react';
import {FaStar} from 'react-icons/fa'

const Star = ({selected = false}) => (
    <>
        <FaStar color={selected ? "red" : "grey"} id="star"/>
    </>
);

export default Star