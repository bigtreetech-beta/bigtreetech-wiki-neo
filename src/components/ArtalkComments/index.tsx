import React, { useEffect } from 'react';
import { useLocation } from '@docusaurus/router';
import { useColorMode } from '@docusaurus/theme-common';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Artalk from 'artalk';
import 'artalk/Artalk.css';

export default function ArtalkComments() {
    const location = useLocation();
    const { colorMode } = useColorMode();
    const { i18n } = useDocusaurusContext();

    const localeMap: Record<string, string> = {
        'en': 'en-US',
        'zh-Hans': 'zh-CN',
    };

    const artalkLocale = localeMap[i18n.currentLocale] || 'en-US';

    useEffect(() => {
        if (typeof window === 'undefined') return;

        const artalk = Artalk.init({
            el: '#artalk-container',
            pageKey: location.pathname,
            pageTitle: document.title,
            server: 'https://artcdn.bttwiki.com',
            site: 'bttwiki',
            darkMode: colorMode === 'dark',
            useBackendConf: false,
            locale: artalkLocale,
            imgUpload: false,
            emoticons: false,
        });

        return () => artalk.destroy();
    }, [location.pathname, colorMode, i18n.currentLocale]);

    return <div id="artalk-container" />;
}
