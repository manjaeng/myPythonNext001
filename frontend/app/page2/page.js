"use client";
import { useEffect, useState } from 'react';

export default function Home() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/hello/')
            .then(res => res.json())
            .then(data => setMessage(data.message))
            .catch(err => console.error(err));
    }, []);

    return (
        <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
            <h1>Django + Next.js 연동</h1>
            <p>API 메시지: {message}</p>
        </div>
    );
}