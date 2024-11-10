# %%
"""Note-taking for Chapter 2 'Introduction to Python' & exercises."""

# *Date: 17/10/24*
# ### Summary on Introduction to Python
#
# #### What is Python
# - A free programming language with open-source code.
# - Created by Guido van Rossum in 1991.
# - An interpreted, high-level general-purpose language.
# - Supports various programming paradigms: procedural, object-oriented, and functional.
#
# #### Main Advantages of Python
# - Ease of learning and use.
# - Readable syntax similar to the English language.
# - Extensive standard library.
# - Cross-platform compatibility.
# - Active developer community.
# - Many ready-to-use libraries and frameworks.
#
# #### Python Versions
# - **Python 2.x**: An outdated version, support ended in 2020.
# - **Python 3.x**: The modern version, actively developed.
#
# #### Ways to Work with Python
# - **Terminal**: The basic way to run Python; convenient for executing individual commands.
# - **IPython Console**: An enhanced version of the terminal with syntax highlighting and multi-line editing.
# - **Spyder IDE**: An integrated development environment for writing and debugging code; allows for line-by-line or cell execution.
# - **Jupyter Notebook**: A web application for interactive development; combines code, text, and visualizations.
#
# #### Installing Python
# - It is recommended to use the **Anaconda** distribution.
# - Includes Python and many useful libraries.
# - Available for Windows, macOS, and Linux.
# - Contains all the necessary tools for development.
#
# #### Jupyter Notebook
# - A web application for creating interactive documents.
# - Supports the combination of code, text, and visualizations.
# - **Types of Cells**:
#   - **Code**: For code.
#   - **Markdown**: For formatted text.
#   - **Raw**: For unformatted text.
# - Convenient for teaching and presenting results.
#
# #### Philosophy of Python
# - "Beautiful is better than ugly."
# - "Explicit is better than implicit."
# - "Simple is better than complex."
# - "Readability counts."
#
# ### Conclusion
# Python is a powerful and flexible tool that requires familiarity with various development environments and the philosophy of the language. It is recommended to install and master the tools described in this summary for effective learning and practice.

# # Exercises
#
# ## 2.1. Answers to Questions
#
# 1. **Is Python open-source software the same as free software?**
#    - Yes, Python is free open-source software, but not all free software is open-source. Free software can be proprietary, while open-source software is always available for modification and distribution.
#
# 2. **Do all free software programs have open source? If not, what is the difference?**
#    - No, not all free software has open source. The difference is that open-source software allows users to modify and distribute the code, whereas proprietary software provides limited access to the source code.
#
# 3. **Python supports dynamic typing. What does that mean?**
#    - Dynamic typing means that the type of a variable is determined at runtime rather than beforehand. This allows for more flexible work with variables but can lead to errors related to incorrect type usage.
#
# 4. **Name the 5 most popular programming languages for data analysis specialists.**
#    - **Python**
#    - **R**
#    - **SQL**
#    - **Java**
#    - **SAS**
#
# 5. **What is the advantage of Python compared to the C language?**
#    - Python offers a simpler and more readable syntax, making it easier to learn and develop. Additionally, Python has a rich standard library and numerous third-party libraries for data processing and machine learning.
#
# 6. **Python is portable. What does "portability" mean in this context?**
#    - Portability means that Python can run on various platforms (Windows, macOS, Linux) without needing to change the code.
#
# 7. **What is the difference between an "extensible" and an "embedded" language?**
#    - An extensible language allows users to add new features and modules, while an embedded language can be integrated into other applications to add programming functionality.
#
# 8. **What is the purpose of an IDE? How does it differ from the command line?**
#    - An IDE (Integrated Development Environment) provides tools for writing, debugging, and testing code in a user-friendly interface. The command line allows for direct execution of commands but does not offer graphical tools or automation features.
#
# 9. **How do you open an existing Jupyter Notebook document? How does this procedure differ from opening a PDF or text file?**
#    - To open a Jupyter Notebook document, you need to start the Jupyter server and use a browser to access the file. This differs from opening a PDF or text file, which can be opened directly with the appropriate applications.
#
# 10. **What is the difference between "Markdown cells" and "code cells" in Jupyter Notebook? What are they used for?**
#     - Markdown cells are used for writing text, descriptions, and formulas, while code cells are intended for writing and executing code. This allows for the combination of textual information and program code in a single document.
#
# ## 2.2. True or False
#
# 1. **The programming language Python was named after the python snake.**
#    - False. Python was named after the television show "Monty Python's Flying Circus."
#
# 2. **Python is a high-level general-purpose language.**
#    - True.
#
# 3. **Python is compiled and not interpreted.**
#    - False. Python is interpreted, although it can also be compiled to bytecode.
#
# 4. **In Python, the command two + two will return Four.**
#    - False. The command will return 4, but the correct syntax is `2 + 2`.
#
# 5. **The IPython console is similar to a command line window.**
#    - True.
#
# 6. **Graphs displayed in a Jupyter Notebook document appear within the document itself.**
#    - True.
#
# 7. **The Anaconda package comes with Chrome and Firefox browsers.**
#    - False. Anaconda does not include browsers.
#
# 8. **"Simple is better than complex" is one of the philosophies of Python.**
#    - True.
#
# 9. **The acronym FLOSS stands for "Free/Libre and Open Source Software."**
#    - True.
#
# 10. **Python supports ONLY object-oriented programming.**
#     - False. Python supports multiple paradigms, including procedural and functional programming.

# *Дата: 17/10/24*
# ### Конспект по введению в Python
#
#
# #### Что такое Python
# - Бесплатный язык программирования с открытым исходным кодом.
# - Создан Гвидо ван Россумом в 1991 году.
# - Интерпретируемый язык высокого уровня общего назначения.
# - Поддерживает различные парадигмы программирования: структурное, объектно-ориентированное, функциональное.
#
# #### Основные преимущества Python
# - Простота изучения и использования.
# - Читаемый синтаксис, похожий на английский язык.
# - Большая стандартная библиотека.
# - Кроссплатформенность.
# - Активное сообщество разработчиков.
# - Множество готовых библиотек и фреймворков.
#
# #### Версии Python
# - **Python 2.x**: устаревшая версия, поддержка прекращена в 2020 году.
# - **Python 3.x**: современная версия, активно развивается.
#
# #### Способы работы с Python
# - **Терминал**: базовый способ запуска Python; удобен для выполнения отдельных команд.
# - **IPython Console**: улучшенная версия терминала с подсветкой синтаксиса и многострочным редактированием.
# - **Spyder IDE**: интегрированная среда разработки для написания и отладки кода; позволяет выполнять код построчно или по ячейкам.
# - **Jupyter Notebook**: веб-приложение для интерактивной разработки; комбинирует код, текст и визуализации.
#
# #### Установка Python
# - Рекомендуется использовать дистрибутив **Anaconda**.
# - Включает Python и множество полезных библиотек.
# - Доступен для Windows, macOS и Linux.
# - Содержит все необходимые инструменты для разработки.
#
# #### Jupyter Notebook
# - Веб-приложение для создания интерактивных документов.
# - Поддерживает комбинирование кода, текста и визуализаций.
# - **Типы ячеек**:
#   - **Code**: для кода.
#   - **Markdown**: для форматированного текста.
#   - **Raw**: для неформатированного текста.
# - Удобен для обучения и презентации результатов.
#
# #### Философия Python
# - "Красивое лучше, чем уродливое".
# - "Явное лучше, чем неявное".
# - "Простое лучше, чем сложное".
# - "Читаемость имеет значение".
#
# ### Заключение
# Python — мощный и гибкий инструмент, который требует знакомства с различными средами разработки и философией языка. Рекомендуется установить и освоить инструменты, описанные в конспекте, для эффективного обучения и практики.

# # Упражнения
#
# ## 2.1. Ответы на вопросы
#
# 1. **Python - это программное обеспечение с открытым исходным кодом. Это то же самое, что и бесплатное ПО?**
#    - Да, Python является бесплатным программным обеспечением с открытым исходным кодом, но не все бесплатные программы имеют открытый исходный код. Бесплатное ПО может быть проприетарным, а открытое ПО всегда доступно для модификации и распространения.
#
# 2. **У всех ли бесплатных программ открытый исходный код? А если нет, то в чем разница?**
#    - Нет, не у всех бесплатных программ открытый исходный код. Разница заключается в том, что открытое ПО позволяет пользователям изменять и распространять код, тогда как проприетарное ПО предоставляет лишь ограниченный доступ к исходному коду.
#
# 3. **Python поддерживает динамическую типизацию. Что это такое?**
#    - Динамическая типизация означает, что тип переменной определяется во время выполнения программы, а не заранее. Это позволяет более гибко работать с переменными, но может привести к ошибкам, связанным с неправильным использованием типов.
#
# 4. **Назовите 5 самых популярных языков программирования для специалистов по анализу данных.**
#    - **Python**
#    - **R**
#    - **SQL**
#    - **Java**
#    - **SAS**
#
# 5. **В чем заключается преимущество Python по сравнению с языком С?**
#    - Python предлагает более простой и читаемый синтаксис, что облегчает обучение и разработку. Кроме того, Python имеет богатую стандартную библиотеку и множество сторонних библиотек для обработки данных и машинного обучения.
#
# 6. **Python портативен. Что в этом контексте означает «портативность»?**
#    - Портативность означает, что Python может выполняться на различных платформах (Windows, macOS, Linux) без необходимости изменения кода.
#
# 7. **В чем разница между «расширяемым» и «встраиваемым» языком?**
#    - Расширяемый язык позволяет пользователям добавлять новые функции и модули, в то время как встраиваемый язык можно интегрировать в другие приложения, чтобы добавить программные функции.
#
# 8. **В чем смысл IDE? Чем она отличается от командной строки?**
#    - IDE (интегрированная среда разработки) предоставляет инструменты для написания, отладки и тестирования кода в удобном интерфейсе. Командная строка позволяет выполнять команды напрямую, но не предлагает графические инструменты и функции автоматизации.
#
# 9. **Как открыть существующий документ Jupyter Notebook? Чем эта процедура отличается от открытия PDF-файла или текстового файла?**
#    - Чтобы открыть документ Jupyter Notebook, необходимо запустить сервер Jupyter и использовать браузер для доступа к файлу. Это отличается от открытия PDF-файла или текстового файла, которые могут быть открыты напрямую с помощью соответствующих приложений.
#
# 10. **В чем разница между «ячейками разметки Markdown» и «ячейками кода» в Jupyter Notebook? Для чего они нужны?**
#     - Ячейки разметки Markdown используются для написания текста, описаний и формул, в то время как ячейки кода предназначены для написания и выполнения кода. Это позволяет сочетать текстовую информацию и программный код в одном документе.
#
# ## 2.2. Правда или ложь
#
# 1. **Язык программирования Python был назван в честь змеи питон.**
#    - Ложь. Python был назван в честь телевизионного шоу "Monty Python's Flying Circus".
#
# 2. **Python - это высокоуровневый язык общего назначения.**
#    - Правда.
#
# 3. **Python компилируется и не интерпретируется.**
#    - Ложь. Python интерпретируется, хотя также может быть скомпилирован в байт-код.
#
# 4. **В Python команда два + два вернет Четыре.**
#    - Ложь. Команда вернет 4, но правильный синтаксис — это `2 + 2`.
#
# 5. **Консоль IPython аналогична окну командной строки.**
#    - Правда.
#
# 6. **Графики, выводимые в документе Jupyter Notebook, отображаются внутри самого документа.**
#    - Правда.
#
# 7. **В комплекте с пакетом Anaconda идут браузеры Chrome и Firefox.**
#    - Ложь. Anaconda не включает браузеры.
#
# 8. **«Простое лучше, чем сложное» - это одна из философий Python.**
#    - Правда.
#
# 9. **Аббревиатура FLOSS означает «Free/Libre and Open Source Software».**
#    - Правда.
#
# 10. **Python поддерживает ТОЛЬКО объектно-ориентированное программирование.**
#     - Ложь. Python поддерживает несколько парадигм, включая процедурное и функциональное программирование.
