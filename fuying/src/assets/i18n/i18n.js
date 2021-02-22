import Vue from "vue";
import VueI18n from "vue-i18n";
import en from "./lang/en";
import cn from "./lang/cn";

Vue.use(VueI18n);

const messages = {
  en: en,
  cn: cn
};

const i18n = new VueI18n({
  locale: localStorage.getItem("lang") || "cn",
  //从sessionStorage中拿到用户的语言选择，如果没有，那默认中文。
  messages,
  silentTranslationWarn: true
});

export default i18n;
