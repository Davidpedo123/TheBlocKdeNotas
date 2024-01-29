import React, { useEffect, useState } from 'react';

export default function Board() {
    const [notas, setNotas] = useState('');

    useEffect(() => {
        fetch('/notas/')
            .then(response => response.json())
            .then(data => {
                let notas = '';
                data.forEach(value => {
                    if (value.id === 3) {
                        notas += `<p>ID: ${value.id}</p>`;
                        notas += `<p>Titulo: ${value.Titulo}</p>`;
                        notas += `<p>contenido: ${value.contenido}</p>`;
                        notas += `<p>fecha_creacion: ${value.fecha_creacion}</p>`;
                        notas += `<p>fecha_modificacion: ${value.fecha_modificacion}</p>`;
                        notas += `<p>audios: ${value.audio}</p>`;
                    }
                });
                setNotas(notas);
            });
    }, []);

    return (
        <section className="bg-neutral-900 min-h-dvh min-w-full" dangerouslySetInnerHTML={{ __html: notas }} />
    );
}
