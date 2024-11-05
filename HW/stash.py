# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
"""Detailed explaining git stash, от Чингиза."""

# %% [markdown]
# ### Что такое стэш?
#
# Команда git stash позволяет на время «сдать в архив» (или отложить) изменения, сделанные в рабочей копии, чтобы вы могли применить их позже. Откладывание изменений полезно, если вам необходимо переключить контекст и вы пока не готовы к созданию коммита.
#
# ### What is stash
#
# git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on. Stashing is handy if you need to quickly switch context and work on something else, but you're mid-way through a code change and aren't quite ready to commit.

# %% [markdown]
# ### Как сохранить стэш ?
#
# Команда `git stash` сохраняет неподтвержденные изменения (индексированные и неиндексированные) в отдельном хранилище, чтобы вы могли вернуться к ним позже. Затем происходит откат до исходной рабочей копии
#
# ### How to save stash ?
#
# The git stash command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.

# %% [markdown]
# ### Как восстановить стэш ?
#
# Чтобы восстановить последний сохранённый стэш, используется команда: `git stash apply`
#
# ### How to Restore a Stash?
#
# To restore the latest stash, use: `git stash apply`

# %% [markdown]
# ### Различие между стэшем и коммитом
#
# **Коммит** — это сохранение зафиксированной версии проекта с историей изменений, привязанной к репозиторию. Коммиты обычно используются для завершённых изменений, которые являются частью общей истории проекта.
#
# **Стэш** — это временное сохранение работы, которое не добавляется в историю. Это удобно, когда вы работаете над чем-то, что ещё не готово к фиксации, или когда необходимо переключиться на другую задачу без потери прогресса.
#
#
# ### Difference Between a Stash and a Commit
#
# **A commit** saves a finalized version of the project with a history record in the repository. Commits are generally used for completed changes that are part of the project's history.
#
# **A stash** is a temporary save of work that isn’t added to history. It’s useful when working on something that isn't ready for a commit, or when you need to switch tasks without losing your progress.

# %% [markdown]
# ### Как просмотреть список сохранённых стэшей?
#
# Чтобы увидеть все сохранённые стэши, используйте: `git stash list`
#
# ### How to View a List of Saved Stashes?
#
# To view all saved stashes, use: `git stash list`

# %% [markdown]
# ### Как удалить стэш?
#
# Удалить определённый стэш можно командой: `git stash drop stash@{index}`
#
# Где `index` — номер стэша в списке, например, `stash@{0}` для последнего стэша.
#
# Для удаления всех стэшей сразу используйте: `git stash clear`
#
# ### How to Delete a Stash?
#
# To delete a specific stash, use: `git stash drop stash@{index}`
#
# Where `index` is the stash number in the list, for example, `stash@{0}` for the latest stash.
#
# To delete all stashes at once, use: `git stash clear`
#

# %% [markdown]
# ### Практические примеры использования стэша
#
# #### 1. Переключение между ветками для срочной правки.
#
# Вы работаете над новой функцией, но вас просят исправить баг в другой ветке. Чтобы не потерять текущие изменения, вы сохраняете их в стэш, переключаетесь на нужную ветку, исправляете баг, делаете коммит, возвращаетесь к своей ветке и восстанавливаете стэш.
#
# #### 2. Удаление незавершённых изменений.
#
# Если вы начали делать какие-то изменения, но решили, что они не нужны, можно сохранить их в стэш, а затем удалить, чтобы вернуться к чистому состоянию рабочей директории.
#
# #### 3. Тестирование проекта на чистой версии.
#
# Вы можете сохранить изменения в стэш и запустить тесты на чистой версии кода, чтобы убедиться, что базовая версия не имеет ошибок.
#
#
# ### Practical Examples of Using a Stash
#
# #### 1. Switching branches for an urgent fix.
#
# You’re working on a new feature, but you’re asked to fix a bug on another branch. To avoid losing your current work, you stash it, switch to the needed branch, fix the bug, commit the fix, return to your branch, and reapply the stash.
#
# #### 2. Removing incomplete changes.
#
# If you started making changes but decide you don’t need them, you can stash them and delete them afterward to get back to a clean state.
#
# #### 3. Testing the project in a clean version.
#
# You might want to stash your changes and run tests on a clean version of the code to ensure the baseline is error-free.
