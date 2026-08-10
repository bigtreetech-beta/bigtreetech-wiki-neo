declare const en: {
    title: string;
    name: string;
    email: string;
    link: string;
    placeholder: string;
    send: string;
    sending: string;
    captcha: string;
    captchaPlaceholder: string;
    captchaPrompt: string;
    reloadCaptcha: string;
    confirm: string;
    cancel: string;
    success: string;
    required: string;
    invalidEmail: string;
    captchaRequired: string;
    captchaInvalid: string;
    commentFail: string;
    networkFail: string;
    restoredMsg: string;
};

export declare const init: typeof MeowComments.init;

declare class MeowComments {
    private readonly element;
    private readonly view;
    private readonly statusId;
    private readonly cleanups;
    private config;
    private state;
    private dialog;
    private mediaCleanup;
    private statusTimer;
    private resizeTimer;
    private tabTimer;
    private destroyed;
    constructor(config: MeowCommentsConfig);
    static init(config: MeowCommentsConfig): MeowComments;
    getConf(): MeowCommentsConfig;
    getEl(): HTMLElement;
    update(config: Partial<MeowCommentsConfig>): void;
    destroy(): void;
    private getMessages;
    private listen;
    private bindEvents;
    private setupDarkMode;
    private syncView;
    private syncInput;
    private renderStatus;
    private setStatus;
    private scheduleStatusClear;
    private queueTextareaResize;
    private adaptTextareaHeight;
    private renderCaptchaDialog;
    private syncCaptchaDialog;
    private closeCaptchaDialog;
    private loadCaptcha;
    private handleRefreshCaptcha;
    private submitComment;
    private handleCaptchaConfirm;
}
export default MeowComments;

export declare interface MeowCommentsConfig {
    /** Element selector or element used to mount MeowComments. */
    el: string | HTMLElement;
    /** Comment server URL only; the frontend appends `/api` automatically. */
    baseUrl?: string;
    /** Artalk-compatible dark mode switch. `auto` follows the system preference. */
    darkMode?: boolean | "auto";
    /** Locale such as `zh-Hans`, `en`, or `auto`. Unknown locales fall back to English. */
    locale?: string;
    /** Page path used to group comments, equivalent to Artalk's `pageKey`. */
    pageKey?: string;
    /** Override the page title sent to the one-way comment API. */
    pageTitle?: string;
    /** `auto` discovers whether the server requires a CAPTCHA on the first submit. */
    captcha?: "auto" | "required" | "disabled";
    rememberUser?: boolean;
    messages?: Partial<MeowCommentsMessages>;
}

export declare type MeowCommentsMessages = typeof en;

export { }
