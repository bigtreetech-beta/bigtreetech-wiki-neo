Prism.languages.klipper_cfg = {
    'comment': /[;#].*/,
    'section': {
        pattern: /(^[ \t]*)\[.+\]/m,
        lookbehind: true,
        alias: 'selector',
        inside: {
            'regex': /\\\\[\[\]{},!?.*]/, // Escape special characters with '\\'
            'operator': /[!?]|\.\.|\*{1,2}/,
            'punctuation': /[\[\]{},]/
        }
    },
    'canuuid': [
        // gpio
        {
            pattern: /11aa22bb33cc/,
            greedy: true
        },
    ],
    'klipper_pin': [
        {
            pattern: /[\^~!]*(ar|analog)\d{1,2}|[\^~!]*(z:)?[a-z]{1,2}\d{1,2}(\.\d{1,2})?/i,
            greedy: true
        },
    ],
    'klipper_num': [
        {
            pattern: /(\-?\d+([\.,]\d+)?\b|\-?[\.,]\d+?)\b/,
            greedy: true
        },
    ],
    'klipper_sensor': [
        {
            pattern: /\b(EPCOS 100K B57560G104F|PT1000|MAX31865)\b/,
            greedy: true
        },
    ],
    'klipper_section_config': {
        pattern: /^\w+\s*[:=]\s*.+$/m,
        inside: {
            'variable': /^\w+/,
            'value': {
                pattern: /[:=]\s*.+$/,
                inside: {
                    'klipper_sensor': /\b(EPCOS 100K B57560G104F|PT1000|MAX31865)\b/i,
                    'klipper_pin': /[\^~!]*(ar|analog)\d{1,2}|[\^~!]*(z:)?[a-z]{1,2}\d{1,2}(\.\d{1,2})?/i,
                    'serial': /\/dev\/serial\/by-(id|path)\/[\d\w\/\-:\.]+/,
                    'canuuid': /11aa22bb33cc/,
                    'number': /\-?\d+([\.,]\d+)?\b|\-?[\.,]\d+?\b/,
                    'boolean': /\b(true|false)\b/i,
                    'comment': /[;#].*/,
                }
            }
        }
    },

};
