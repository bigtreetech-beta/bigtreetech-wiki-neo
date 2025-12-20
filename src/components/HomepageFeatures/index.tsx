import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  // Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Board',
    // Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        <a href="./docs/intro">
          <img
            src={require('@site/static/img/maxez-main.webp').default}
            alt=""
          />
          <br/>
        </a>
      </>
    ),
  },
  {
    title: 'Extruder',
    // Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        <a href="./docs/extruder">
          <img
            src={require('@site/static/img/h2-v2x.webp').default}
            alt=""
          />
          <br/>
        </a>
      </>
    ),
  },
  {
    title: 'Module',
    // Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        <a href="./docs/module">
          <img
            src={require('@site/static/img/lis2dw-main.webp').default}
            alt=""
          />
          <br/>
        </a>
      </>
    ),
  },
];

// function Feature({title, Svg, description}: FeatureItem) {

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      {/* <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div> */}

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
