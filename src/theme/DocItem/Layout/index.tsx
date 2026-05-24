import React, { type ReactNode } from 'react';
import Layout from '@theme-original/DocItem/Layout';
import type LayoutType from '@theme/DocItem/Layout';
import type { WrapperProps } from '@docusaurus/types';

// check if is production
const isProd = process.env.NODE_ENV === 'production';

type Props = WrapperProps<typeof LayoutType>;

export default function LayoutWrapper(props: Props): ReactNode {
    return (
        <>
            <Layout {...props} />
            <br />
            {isProd ? (
                <ArtalkBlock />
            ) : (
                <Placeholder />
            )}
        </>
    );
}

function ArtalkBlock() {
    const [visible, setVisible] = React.useState(false);
    const ref = React.useRef<HTMLDivElement>(null);

    React.useEffect(() => {
        if (!ref.current) return;

        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) {
                setVisible(true);
                observer.disconnect();
            }
        });

        observer.observe(ref.current);

        return () => observer.disconnect();
    }, []);

    const ArtalkComments = React.lazy(() =>
        import('@site/src/components/ArtalkComments')
    );

    return (
        <div className="col col--9" ref={ref}>
            {visible ? (
                <React.Suspense fallback={null}>
                    <ArtalkComments />
                </React.Suspense>
            ) : null}
        </div>
    );
}

function Placeholder() {
    return (
        <div className="col col--9">
            <div
                style={{
                    padding: '12px',
                    border: '1px dashed #727272',
                    borderRadius: 8,
                    color: '#b8b8b8',
                }}
            >
                DEV MODE Artalk Not Init
            </div>
        </div>
    );
}
