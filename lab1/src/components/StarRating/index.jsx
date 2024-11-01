import React from 'react';
import Star from '../Star';

const createArray = length => [...Array(length)];

export default function StarRating({totalStars=10, selectedStars=0, onRate = f => f})
{
    return (
        <>
            {createArray(totalStars).map((n,i) => (
                <Star
                    key = {i}
                    selected = {selectedStars > i}
                    onSelect = {() => selectedStars<10 ? onRate(selectedStars+1) : onRate(0)}
                />
            ))}
        </>
    )
}