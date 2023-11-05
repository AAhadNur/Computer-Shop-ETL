import unittest
from airflow.models import DagBag


class TestMyDataPipelineDag(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag(
            dag_folder='/home/a_ahad/Desktop/Workshop/Computer-Shop/Computer-Shop/dags')

    def test_dag_loaded(self):
        dag_id = 'my_datapipeline_dag'
        self.assertTrue(dag_id in self.dagbag.dags)

    def test_tasks(self):
        dag = self.dagbag.dags['my_datapipeline_dag']
        tasks = dag.tasks
        task_ids = [task.task_id for task in tasks]

        expected_task_ids = ['crawl_ryans', 'crawl_startech',
                             'extract_data', 'transform_data', 'load_data']
        for task_id in expected_task_ids:
            self.assertIn(task_id, task_ids)

    def test_dependencies(self):
        dag = self.dagbag.dags['my_datapipeline_dag']
        extract_task = dag.get_task('extract_data')
        upstream_task_ids = [
            task.task_id for task in extract_task.upstream_list]
        expected_upstream_tasks = ['crawl_ryans', 'crawl_startech']

        for task_id in expected_upstream_tasks:
            self.assertIn(task_id, upstream_task_ids)


if __name__ == '__main__':
    unittest.main()
