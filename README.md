# FAIR-DB Website

## Paper Abstract
In our everyday lives, technologies based on data play an increasingly important role. With the widespread adoption of decision making systems also in very sensitive environments, Fairness has become a very important topic of discussion within the data science community. In this context, it is crucial to ensure that the data on which we base these decisions, are fair, and do not reflect historical biases.  

In this demo we propose FAIR-DB (FunctionAl dependencIes to discoveR Data Bias), a system that exploiting the notion of Functional Dependency, a particular type of constraint on the data, can discover unethical behaviours in a dataset.

The proposed solution is implemented as a web-based application, that, given an input dataset, generates such dependencies, walks the user trough their analysis, and finally provides many insights about bias present in the data. 
Our tool uses a novel metric to evaluate the unfairness present in datasets, identifies the attributes that encompass discrimination (e.g. ethnicity, sex or religion), and provides very precise information about the groups treated unequally. We also provide a detailed description of the system architecture and present a demonstration scenario, based on a real-world dataset frequently used in the field of computer ethics.

## User Section
Are you confused? Why don't you look at our demo video? It could be helpful in understanding how the system works.

https://user-images.githubusercontent.com/37806290/151364199-9791e511-e7c7-452d-ab44-61e8970ecd33.mp4


If you want to use the python notebook version here is the Github repository link: https://github.com/chiaracriscuolo/FAIR-DB-Notebook.

## Developer Section
## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out the [documentation](https://nuxtjs.org).

## Special Directories

You can create the following extra directories, some of which have special behaviors. Only `pages` is required; you can delete them if you don't want to use their functionality.

### `assets`

The assets directory contains your uncompiled assets such as Stylus or Sass files, images, or fonts.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/assets).

### `components`

The components directory contains your Vue.js components. Components make up the different parts of your page and can be reused and imported into your pages, layouts and even other components.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/components).

### `layouts`

Layouts are a great help when you want to change the look and feel of your Nuxt app, whether you want to include a sidebar or have distinct layouts for mobile and desktop.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/layouts).


### `pages`

This directory contains your application views and routes. Nuxt will read all the `*.vue` files inside this directory and setup Vue Router automatically.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/get-started/routing).

### `plugins`

The plugins directory contains JavaScript plugins that you want to run before instantiating the root Vue.js Application. This is the place to add Vue plugins and to inject functions or constants. Every time you need to use `Vue.use()`, you should create a file in `plugins/` and add its path to plugins in `nuxt.config.js`.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/plugins).

### `static`

This directory contains your static files. Each file inside this directory is mapped to `/`.

Example: `/static/robots.txt` is mapped as `/robots.txt`.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/static).

### `store`

This directory contains your Vuex store files. Creating a file in this directory automatically activates Vuex.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/store).
