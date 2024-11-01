import React from 'react';
import Star from '../Star';

const createArray = length => [...Array(length)];

export default function StarRating({totalStars=10, selectedStars=0})
{
    return (
        <>
            {createArray(totalStars).map((n,i) => (
                <Star
                    key = {i}
                    selected = {selectedStars > i}
                />
            ))}
        </>
    )
}