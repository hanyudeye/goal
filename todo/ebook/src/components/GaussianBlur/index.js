import React from 'react';
import styles from './style.less';

export default ({
    children,

}) => (
    <div
        className={styles.bg}
    >
        {children}
        你好，同学
    </div>

);