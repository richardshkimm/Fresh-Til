import type { NextPage } from 'next'
import Head from 'next/head'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Fresh &lsquo;Til</title>
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>

      <header className={styles.header}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          LOGO  Home  Profile  Settings
        </a>
      </header>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Hello, <a href="">User!</a>
        </h1>

        <div className={styles.description}>
          <h2>Your Inventory</h2>
        </div>

      </main>
    </div>
  )
}

export default Home
