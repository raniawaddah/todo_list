from odoo import fields, models, api, _

class TodoTask(models.Model):
    _name = 'todo.task'
    _rec_name = 'task_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    task_name = fields.Char()
    active = fields.Boolean(default=True)

    description = fields.Text()
    due_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    assign_to_id = fields.Many2one('res.users', )
    estimated_time = fields.Float()
    line_ids = fields.One2many('todo.line', 'todo_id')




    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ], default='new', string='Status',)

    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'


    def check_due_date(self):
        todo_task_ids = self.search([])
        for rec in todo_task_ids:
            if rec.state and rec.state in ('new, in_progress') and rec.due_date < fields.date.today():
                rec.is_late = True
            else:
                rec.is_late = False




    class TodoLine(models.Model):
        _name = 'todo.line'

        todo_id = fields.Many2one('todo.task')
        date = fields.Date()
        description = fields.Char()
        time = fields.Float()



