import React, { useState, useEffect } from "react";

const loadJSON = (key) => key && JSON.parse(localStorage.getItem(key));
const saveJSON = (key, data) => localStorage.setItem(key, JSON.stringify(data));

export function FetchData() {
    const [data, setData] = useState(loadJSON("catImages") || []);

    useEffect(() => {
        if(data.length > 0) return;
        fetch(`https://api.thecatapi.com/v1/images/search?limit=10`)
        .then(response => response.json())
        .then((data) => {
            data = data.map(({ id, url, width }) => ({ id, url, width }));
            setData(data);
            saveJSON("catImages", data);
        })
        .catch(console.error);
    }, []);

    useEffect(() => {
        if (data.length) {
            saveJSON("catImages", data);
        }
    }, [data]);

    // if(data)
    //     return <pre>{JSON.stringify(data,null,2)}</pre>

    if(data) return data;
}
