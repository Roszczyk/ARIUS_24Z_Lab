import React from 'react';

const HandleEvent = () => {
    const onSubmit = (e) => {
        e.preventDefault();
        console.log("on submit");
        console.log(e);
    }
    return (
        <form onSubmit = {onSubmit}>
            <button>Wyślij</button>
        </form>
    )
}

export default HandleEvent;
