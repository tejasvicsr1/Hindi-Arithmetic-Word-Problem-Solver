verbname = ['है', 'होना', 'खरीदा', 'दिया', 'उठाया', 'बढा', 'खर्चा', 'ढूंढा', 'भुगतान', 'उगाया', 'जा', 'खेला', 'ला', 'काटा', 'काम', 'बेचा', 'खरीदना', 'रखा', '*', 'बनाया', '*', 'पकडा', 'परोसा', 'कमाया', 'उधार', 'बचाया', 'मिला', 'जा', 'उपस्थित', 'देखा', 'रखा', 'खाया', 'कीमत', 'जीता', 'हारा', 'किया', 'किराया', 'ज़रूरत', 'लिया', 'खड़ा', 'खतम', 'डालना', 'बुलाया', 'तोडा', 'चमका', 'रखना', 'शुरु', 'बाटना', 'आना', 'भरना', 'साफ', 'जोड़ना', 'हार', 'टूटना', 'निशचित', 'फटना', 'शुरु', 'खतम', 'इकठ्ठा', 'ज़रूरत',
            'चाहना', '*', 'पूछना', 'नियंत्रित', 'शामिल', 'भार', 'इस्तमाल', 'चल', 'बनाना', 'बारिश', 'भागा', 'दौडा', 'टपकना', 'पीना', 'चढ़ना', 'फसल', 'दौडा', 'उतरना', 'इकठ्ठा', 'डालना', 'रंगना', 'बाकी', 'वापस', 'नापा', 'देखा', 'गिराना', 'हिलाना', 'जोडा', '*', '*', 'ढकना', 'कमना', 'बढाना', '*', 'झेलना', 'खिलाना', 'पढना', 'ठीक', 'बनाना', 'जाना', 'स्वामित्व', '*', 'बसना', 'अंकित', 'बोना', 'देना', 'जीना', 'उठाना', '*', 'गोद', 'चलाना', '*', 'परिणाम', 'खरीदना', 'खरीदना', 'ज़रुरत', 'घूमना', 'भागना', 'दौडना', 'फाडना']
verbtype = ['0', '0', 't+', 't-', 't+', '+', '--', '+', 't-', 't-', '+', '+', 't+', '--', '+', 't-', 't+', 't-', '-', '++', 't+', '+', '-', '+', 't+', '+', 't+', 't-', '+', '+', 't-', '--', '-', '+', '-', '1', 't+', '+', 't+', '+', '+', 't-', '+', '--', '+', 't-', '0', '-', '+', 't-', '+', '++', '-', '-', '+', '-', '+', '+',
            '++', '+', '+', '+', '+', '0', '0', '+', '--', '+', '++', '+', '+', '+', '--', '--', '+', 't+', '+', '+', '++', 't-', '+', '0', 't-', '+', '--', 't-', '+', '+', '+', '+', '+', '--', '++', '+', '+', 't-', '+', '++', '++', '+', '0', 't-', '+', '+', 't-', 't-', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '-']

verbtype[26] = '0'
ind = verbname.index("चल")
verbtype[ind] = '0'
verbname.append("घट")
verbtype.append('-')
verbname.append("बढ")
verbtype.append("+")
verbtype.append("मिल")
verbtype.append("+")
verbtype[13] = '0'
verbtype[71] = '0'
verbtype[67] = '0'
verbname.append("भर")
verbtype.append('+')
verbname.append("निकाल")
verbtype.append('-')
verbname.append("टूटे")
verbtype.append('-')