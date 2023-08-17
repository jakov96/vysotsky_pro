module.exports = {
  css: {
    loaderOptions: {
      sass: {
        prependData: `
        @import "@/assets/sass/styles.scss";
        @import "~@/assets/sass/fonts.scss";
        `,
      },
    },
  },
};
