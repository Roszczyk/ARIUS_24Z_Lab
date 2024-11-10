import React, { useState, useEffect } from "react";

const loadJSON = (key) => key && JSON.parse(localStorage.getItem(key));
const saveJSON = (key, data) => localStorage.setItem(key, JSON.stringify(data));

export function FetchData({ id }) {
    const [data, setData] = useState(loadJSON(`cat:${id}`));

    useEffect(() => {
        if(!data) return;
        const {url, width} = data;
        saveJSON(`cat:${id}`, {
            id,
            url,
            width
        });
    }, [data]);

    useEffect(() => {
        if(!id) return;
        if(data && data.id === id) return;
        fetch(`https://api.thecatapi.com/v1/images/${id}`)
        .then(response => response.json())
        .then(response1 => setData(response1))
        .catch(console.error);
    }, [id]);

    if(data)
        return <pre>{JSON.stringify(data,null,2)}</pre>
}
