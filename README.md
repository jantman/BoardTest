# BoardTest
Testing various GitHub kanban boards

* [HuBoard](https://huboard.com/) - [https://huboard.com/jantman/BoardTest/](https://huboard.com/jantman/BoardTest/)
* [waffle.io](https://waffle.io/) - [https://waffle.io/jantman/BoardTest](https://waffle.io/jantman/BoardTest)
* [zube.io](https://zube.io/) - [https://zube.io/projects/4317/kanban](https://zube.io/projects/4317/kanban)

Features as of commit date on this file:

|                             | HuBoard                               | waffle.io                         | zube.io                                             |
|-----------------------------|---------------------------------------|-----------------------------------|-----------------------------------------------------|
| Multiple Projects per Board | Add repos to existing repo board      | Add repos to existing repo board  | Create "Project" boards, add N repos to them        |
| Column/Status Tracking      | Labels added to repo                  | Labels added to repo              | Internal? Not label-based                           |
| Shows both PRs and Issues   | Yes                                   | Yes                               | Yes                                                 |
| Shows Assigned User(s)      | icon                                  | icon                              | icon                                                |
| Shows Labels                | Color, mouse-over for name            | Color and name                    | Color and name                                      |
| Auto-move to done?          | Yes                                   | Yes                               | Yes, but not for pre-existing issues/PRs            |
| Columns                     | Backlog, Ready, Working, Review, Done | Backlog, Ready, In Progress, Done | Inbox, Backlog, Ready, In Progress, In Review, Done |
| Customizable Columns?       | No                                    | Yes, between Backlog and Done     | No                                                  |
| Filters?                    | Assignee, Milestone, Label            | Assignee, Milestone, Label        | Assignee, Milestone, Label                          |
| Per-Milestone View?         | Yes                                   | No                                | No                                                  |
| Field for card sizing?      | No                                    | Yes                               | No                                                  |

None of the options have an API to retrieve data, and it seems that they store column ordering internally.

For my personal use, Zube had a definite plus by being able to create "Project" boards (i.e. I could have a board for all of my F/OSS projects, though I'd have to manually add them), but lost out because of the lack of customizable columns and internal tracking of card state (with no documented API). That left it down to HuBoard and Waffle. While I *really* like the per-milestone view of HuBoard that makes it easier to drag cards between milestones, I only use them on one of my projects. So, waffle.io it is.
