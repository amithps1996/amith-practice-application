import React, { useState, useEffect } from "react";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetch("/api/data")
            .then((res) => res.json())
            .then((data) => setMessage(data.message));
    }, []);

    return (
        <div style={{ textAlign: "center", marginTop: "20px" }}>
            <h1>Docker Practice App</h1>
            <h2>Message from Backend: {message}</h2>
        </div>
    );
}

export default App;
