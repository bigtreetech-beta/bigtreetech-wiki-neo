import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Translate from '@docusaurus/Translate';

type FeatureItem = {
  title: ReactNode;
  prod_img: string;
  url: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: <Translate>Board</Translate>,
    prod_img: require('@site/static/img/maxez-main.webp').default,
    url: 'docs/intro',
    description: (
      <>
      </>
    ),
  },
  {
    title: <Translate>Extruder</Translate>,
    prod_img: require('@site/static/img/h2-v2x.webp').default,
    url: 'docs/extruder',
    description: (
      <>
      </>
    ),
  },
  {
    title: <Translate>Module</Translate>,
    prod_img: require('@site/static/img/lis2dw-main.webp').default,
    url: 'docs/module',
    description: (
      <>
      </>
    ),
  },
];

function Feature({title, prod_img, url, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <a href={url}>
          <img src={prod_img} width="65%" />
        </a>
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
