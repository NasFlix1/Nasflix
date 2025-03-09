// frontend/pages/index.js
import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Nasflix</title>
      </Head>
      <main className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
        <h1 className="text-4xl font-bold mb-6">Bienvenue sur Nasflix</h1>
        <div className="grid grid-cols-2 gap-4">
          <Link href="/films" className="p-4 bg-gray-700 rounded-lg">Films</Link>
          <Link href="/series" className="p-4 bg-gray-700 rounded-lg">Séries</Link>
          <Link href="/musique" className="p-4 bg-gray-700 rounded-lg">Musique</Link>
          <Link href="/jeux" className="p-4 bg-gray-700 rounded-lg">Jeux</Link>
        </div>
      </main>
    </div>
  );
}

